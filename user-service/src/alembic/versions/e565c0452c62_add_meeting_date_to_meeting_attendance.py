"""Add meeting_date to meeting_attendance

Revision ID: e565c0452c62
Revises: 
Create Date: 2024-12-30 16:02:01.101263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e565c0452c62'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meeting_attendance', sa.Column('meeting_date', sa.Date(), nullable=False))
    op.alter_column('meeting_attendance', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('meeting_attendance', 'meeting_type',
               existing_type=sa.VARCHAR(),
               type_=sa.Enum('SUNDAY_SERVICE', 'GROUP_MEETING', name='meetingtype'),
               nullable=False)
    op.create_foreign_key(None, 'meeting_attendance', 'users', ['user_id'], ['id'])
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'level',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'level',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint(None, 'meeting_attendance', type_='foreignkey')
    op.alter_column('meeting_attendance', 'meeting_type',
               existing_type=sa.Enum('SUNDAY_SERVICE', 'GROUP_MEETING', name='meetingtype'),
               type_=sa.VARCHAR(),
               nullable=True)
    op.alter_column('meeting_attendance', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('meeting_attendance', 'meeting_date')
    # ### end Alembic commands ###