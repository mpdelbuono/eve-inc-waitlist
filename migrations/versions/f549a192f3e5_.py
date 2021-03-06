"""empty message

Revision ID: f549a192f3e5
Revises: ffdd6dd99166
Create Date: 2016-04-12 15:23:01.982000

"""

# revision identifiers, used by Alembic.
revision = 'f549a192f3e5'
down_revision = 'ffdd6dd99166'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comp_history_ext_inv',
    sa.Column('inviteExtID', sa.Integer(), nullable=False),
    sa.Column('waitlistID', sa.Integer(), nullable=True),
    sa.Column('timeCreated', sa.DateTime(), nullable=True),
    sa.Column('timeInvited', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['waitlistID'], [u'waitlists.id'], ),
    sa.PrimaryKeyConstraint('inviteExtID')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comp_history_ext_inv')
    ### end Alembic commands ###
