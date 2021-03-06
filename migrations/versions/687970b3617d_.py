"""empty message

Revision ID: 687970b3617d
Revises: 686609cc9783
Create Date: 2017-02-03 15:58:52.570076

"""

# revision identifiers, used by Alembic.
revision = '687970b3617d'
down_revision = '686609cc9783'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calendar_category',
    sa.Column('categoryID', sa.Integer(), nullable=False),
    sa.Column('categoryName', sa.String(length=50), nullable=True),
    sa.Column('fixedTitle', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('categoryID')
    )
    op.create_index(op.f('ix_calendar_category_categoryName'), 'calendar_category', ['categoryName'], unique=False)
    op.create_table('calendar_event',
    sa.Column('eventID', sa.Integer(), nullable=False),
    sa.Column('eventCreatorID', sa.Integer(), nullable=True),
    sa.Column('eventTitle', mysql.TEXT(), nullable=True),
    sa.Column('eventDescription', mysql.TEXT(), nullable=True),
    sa.Column('eventCategoryID', sa.Integer(), nullable=True),
    sa.Column('eventApproved', sa.Boolean(), nullable=True),
    sa.Column('eventTime', sa.DateTime(), nullable=True),
    sa.Column('approverID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['approverID'], ['accounts.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['eventCategoryID'], ['calendar_category.categoryID'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['eventCreatorID'], ['accounts.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('eventID')
    )
    op.create_index(op.f('ix_calendar_event_eventApproved'), 'calendar_event', ['eventApproved'], unique=False)
    op.create_index(op.f('ix_calendar_event_eventCategoryID'), 'calendar_event', ['eventCategoryID'], unique=False)
    op.create_index(op.f('ix_calendar_event_eventCreatorID'), 'calendar_event', ['eventCreatorID'], unique=False)
    op.create_index(op.f('ix_calendar_event_eventTime'), 'calendar_event', ['eventTime'], unique=False)
    op.create_table('calendar_backseat',
    sa.Column('accountID', sa.Integer(), nullable=True),
    sa.Column('eventID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['accountID'], ['accounts.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['eventID'], ['calendar_event.eventID'], onupdate='CASCADE', ondelete='CASCADE')
    )
    op.create_table('calendar_organizer',
    sa.Column('accountID', sa.Integer(), nullable=True),
    sa.Column('eventID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['accountID'], ['accounts.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['eventID'], ['calendar_event.eventID'], onupdate='CASCADE', ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calendar_organizer')
    op.drop_index(op.f('ix_calendar_event_eventTime'), table_name='calendar_event')
    op.drop_index(op.f('ix_calendar_event_eventCreatorID'), table_name='calendar_event')
    op.drop_index(op.f('ix_calendar_event_eventCategoryID'), table_name='calendar_event')
    op.drop_index(op.f('ix_calendar_event_eventApproved'), table_name='calendar_event')
    op.drop_table('calendar_event')
    op.drop_index(op.f('ix_calendar_category_categoryName'), table_name='calendar_category')
    op.drop_table('calendar_category')
    op.drop_table('calendar_backseat')
    # ### end Alembic commands ###
