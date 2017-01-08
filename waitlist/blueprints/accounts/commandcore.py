import logging
from flask.blueprints import Blueprint
from waitlist.permissions import perm_manager
from flask_login import login_required
from waitlist.base import db
from waitlist.storage.database import Account
from flask.templating import render_template
bp = Blueprint('accounts_cc', __name__)
logger = logging.getLogger(__name__)

@bp.route("/", methods=["GET"])
@login_required
@perm_manager.require('commandcore')
def accounts():
    accounts = db.session.query(Account).filter(Account.disabled == False).order_by(Account.username).all()
    return render_template("waitlist/tools/commandcore_list.html", accounts=accounts)