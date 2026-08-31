"""phone number column adding for users table

Revision ID: b10e81cd7642
Revises: 
Create Date: 2026-08-25 12:33:04.707905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b10e81cd7642'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(20), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
