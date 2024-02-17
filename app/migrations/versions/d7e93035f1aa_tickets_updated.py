"""tickets updated

Revision ID: d7e93035f1aa
Revises: d1c4a1f15540
Create Date: 2024-02-17 18:24:50.489520

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7e93035f1aa'
down_revision: Union[str, None] = 'd1c4a1f15540'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('event_type', sa.Enum('concert', 'museum', 'exhibition', 'other', name='eventtypeenum'), nullable=False))
    op.add_column('tickets', sa.Column('title', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tickets', 'title')
    op.drop_column('tickets', 'event_type')
    # ### end Alembic commands ###
