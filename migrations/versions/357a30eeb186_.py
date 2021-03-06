"""empty message

Revision ID: 357a30eeb186
Revises: 7a51a649d6f9
Create Date: 2017-04-14 14:41:00.685716

"""

# revision identifiers, used by Alembic.
revision = '357a30eeb186'
down_revision = '7a51a649d6f9'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calendar_category', sa.Column('fixedDescription', mysql.TEXT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('calendar_category', 'fixedDescription')
    # ### end Alembic commands ###
