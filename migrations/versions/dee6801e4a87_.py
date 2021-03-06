"""empty message

Revision ID: dee6801e4a87
Revises: 0c6c4b5461ce
Create Date: 2016-05-05 22:10:23.689000

"""

# revision identifiers, used by Alembic.
revision = 'dee6801e4a87'
down_revision = '0c6c4b5461ce'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('send_invite')
    op.add_column('waitlist_entries', sa.Column('inviteCount', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('waitlist_entries', 'inviteCount')
    op.create_table('send_invite',
    sa.Column('sendInviteID', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('characterID', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('fleetID', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('inviteCount', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('sendAt', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['characterID'], [u'characters.id'], name=u'send_invite_ibfk_1'),
    sa.ForeignKeyConstraint(['fleetID'], [u'crest_fleets.fleetID'], name=u'send_invite_ibfk_2'),
    sa.PrimaryKeyConstraint('sendInviteID'),
    mysql_default_charset=u'utf8mb4',
    mysql_engine=u'InnoDB'
    )
    ### end Alembic commands ###
