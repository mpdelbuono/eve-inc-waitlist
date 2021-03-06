"""empty message

Revision ID: cf588e0dfd5c
Revises: 95eb3cae9e68
Create Date: 2016-12-30 21:46:10.941000

"""

# revision identifiers, used by Alembic.
revision = 'cf588e0dfd5c'
down_revision = '95eb3cae9e68'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('displayName', sa.String(length=150), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'displayName')
    ### end Alembic commands ###
