"""empty message

Revision ID: 839456a7e73e
Revises: d58d1159149e
Create Date: 2016-03-06 19:05:54.339000

"""

# revision identifiers, used by Alembic.
revision = '839456a7e73e'
down_revision = 'd58d1159149e'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alliance_bans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('reason', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alliance_bans_name'), 'alliance_bans', ['name'], unique=True)
    op.create_table('apicache_corporationinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('allianceID', sa.Integer(), nullable=True),
    sa.Column('allianceName', sa.String(length=100), nullable=True),
    sa.Column('expire', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_apicache_corporationinfo_allianceID'), 'apicache_corporationinfo', ['allianceID'], unique=False)
    op.create_index(op.f('ix_apicache_corporationinfo_allianceName'), 'apicache_corporationinfo', ['allianceName'], unique=False)
    op.create_index(op.f('ix_apicache_corporationinfo_name'), 'apicache_corporationinfo', ['name'], unique=True)
    op.create_table('apicache_characterinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('corporationID', sa.Integer(), nullable=True),
    sa.Column('corporationName', sa.String(length=100), nullable=True),
    sa.Column('expire', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_apicache_characterinfo_corporationID'), 'apicache_characterinfo', ['corporationID'], unique=False)
    op.create_table('corporation_bans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('reason', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_corporation_bans_name'), 'corporation_bans', ['name'], unique=True)
    op.add_column(u'characters', sa.Column('reason', mysql.TEXT(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'characters', 'reason')
    op.drop_index(op.f('ix_corporation_bans_name'), table_name='corporation_bans')
    op.drop_table('corporation_bans')
    op.drop_index(op.f('ix_apicache_characterinfo_corporationID'), table_name='apicache_characterinfo')
    op.drop_table('apicache_characterinfo')
    op.drop_index(op.f('ix_apicache_corporationinfo_name'), table_name='apicache_corporationinfo')
    op.drop_index(op.f('ix_apicache_corporationinfo_allianceName'), table_name='apicache_corporationinfo')
    op.drop_index(op.f('ix_apicache_corporationinfo_allianceID'), table_name='apicache_corporationinfo')
    op.drop_table('apicache_corporationinfo')
    op.drop_index(op.f('ix_alliance_bans_name'), table_name='alliance_bans')
    op.drop_table('alliance_bans')
    ### end Alembic commands ###
