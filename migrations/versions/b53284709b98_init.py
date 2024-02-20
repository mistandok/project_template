"""init

Revision ID: b53284709b98
Revises: 
Create Date: 2024-02-20 20:07:44.205614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b53284709b98'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'note',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Unicode(100), nullable=False),
        sa.Column('description', sa.Text),
    )


def downgrade() -> None:
    op.drop_table('note')
