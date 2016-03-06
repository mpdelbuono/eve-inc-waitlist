"""empty message

Revision ID: 2e56087b8ba7
Revises: None
Create Date: 2016-03-06 09:38:15.793000

"""

# revision identifiers, used by Alembic.
revision = '2e56087b8ba7'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apicache_characterid',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('eve_name', sa.String(length=100), nullable=True),
    sa.Column('newbro', sa.Boolean(), nullable=False),
    sa.Column('banned', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('eve_name')
    )
    op.create_table('invtypes',
    sa.Column('typeID', sa.Integer(), nullable=False),
    sa.Column('groupID', sa.Integer(), nullable=True),
    sa.Column('typeName', sa.String(length=100), nullable=True),
    sa.Column('description', mysql.LONGTEXT(), nullable=True),
    sa.Column('mass', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('volume', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('capacity', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('portionSize', sa.Integer(), nullable=True),
    sa.Column('raceID', sa.SmallInteger(), nullable=True),
    sa.Column('basePrice', sa.DECIMAL(precision=19, scale=4), nullable=True),
    sa.Column('published', mysql.TINYINT(), nullable=True),
    sa.Column('marketGroupID', sa.BIGINT(), nullable=True),
    sa.Column('iconID', sa.BIGINT(), nullable=True),
    sa.Column('soundID', sa.BIGINT(), nullable=True),
    sa.PrimaryKeyConstraint('typeID')
    )
    op.create_index('invTypes_groupid', 'invtypes', ['groupID'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('is_restrictive', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('waitlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('current_char', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('login_token', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['current_char'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('login_token'),
    sa.UniqueConstraint('username')
    )
    op.create_table('waitlist_entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation', sa.DateTime(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('waitlist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['waitlist_id'], ['waitlists.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('account_roles',
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], onupdate='CASCADE', ondelete='CASCADE')
    )
    op.create_table('fittings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ship_type', sa.Integer(), nullable=True),
    sa.Column('waitlist_id', sa.Integer(), nullable=True),
    sa.Column('modules', sa.String(length=10000), nullable=True),
    sa.Column('comment', sa.String(length=10000), nullable=True),
    sa.ForeignKeyConstraint(['ship_type'], ['invtypes.typeID'], ),
    sa.ForeignKeyConstraint(['waitlist_id'], ['waitlist_entries.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('linked_chars',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('char_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['char_id'], ['characters.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id'], ['accounts.id'], onupdate='CASCADE', ondelete='CASCADE')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('linked_chars')
    op.drop_table('fittings')
    op.drop_table('account_roles')
    op.drop_table('waitlist_entries')
    op.drop_table('accounts')
    op.drop_table('waitlists')
    op.drop_table('roles')
    op.drop_index('invTypes_groupid', table_name='invtypes')
    op.drop_table('invtypes')
    op.drop_table('characters')
    op.drop_table('apicache_characterid')
    ### end Alembic commands ###
