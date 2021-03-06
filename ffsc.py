from multiprocessing import Process, JoinableQueue
from waitlist.storage.database import Shipfit, InvType, FitModule
from waitlist import db, manager


if __name__ == '___main__':
    manager.run()


class ConvertConsumer(Process):
    def __init__(self, tasks, name):
        Process.__init__(self)
        self.__tasks = tasks
        self.name = name

    def run(self):
        while True:
            work = self.__tasks.get()
            if work is None:
                break
            ConvertConsumer.convert(work[0], work[1])

    @staticmethod
    def convert(offset, limit):
        fits = db.session.query(Shipfit).limit(limit).offset(offset).all()
        for fit in fits:
            if fit.modules is not None and fit.modules != '':
                filtered_modules_string = ''
                for moduleDefStr in fit.modules.split(':'):
                    if moduleDefStr == '':
                        continue
                    try:
                        moduleDefArr = moduleDefStr.split(';')
                        if len(moduleDefArr) != 2:
                            print("Skipping Module Fit ID=", fit.id, " Module Def Str:", moduleDefStr)
                            continue
                        
                        # lets check here if that module exists
                        moduleDefArr[0] = int(moduleDefArr[0])
                        moduleDefArr[1] = int(moduleDefArr[1])
                        if moduleDefArr[1] > 2147483647 or moduleDefArr[1] < 0:
                            moduleDefArr[1] = 2147483647
                        
                        module = db.session.query(InvType).get(moduleDefArr[0])
                        if module is None:
                            print("No Module with ID=", str(moduleDefArr[0]))
                            continue
                        
                        dbModule = FitModule(moduleID=moduleDefArr[0], amount=moduleDefArr[1])
                        fit.moduleslist.append(dbModule)
                        filtered_modules_string += str(moduleDefArr[0])+';'+str(moduleDefArr[1])+':'
                    except ValueError as e:
                        print("Fit ID=", str(fit.id), " Module Def Str:", moduleDefStr)
                        raise e
                    except IndexError as ie:
                        print("Fit ID=", str(fit.id), " Module Def Str:", moduleDefStr)
                        raise ie
                
                if filtered_modules_string == '' or filtered_modules_string == '::':
                    filtered_modules_string = ':'
                else:
                    filtered_modules_string += ':'
                if fit.modules != filtered_modules_string:
                    print("Correcting: ", fit.modules, " -> ", filtered_modules_string)
                    fit.modules = filtered_modules_string
        
        db.session.commit()
        db.session.close()


if __name__ == '__main__':
    consumer_threads = []
    task_queue = JoinableQueue(maxsize=100)
    for i in range(6):
        t = ConvertConsumer(task_queue, "dec"+str(i))
        t.start()
        consumer_threads.append(t)
    
    numberOfFits = db.session.query(Shipfit).count()
    stepSize = 1000
    for s in range(0, numberOfFits, stepSize):
        task_queue.put((s, stepSize))
    
    # send them all the signal to break
    for _ in range(6):
        task_queue.put(None)
