"""Iaaa

Revision ID: 398e6ad0dba9
Revises: 85a2bf6daf97
Create Date: 2024-01-13 20:31:06.786208

"""
from typing import Sequence, Union

from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "398e6ad0dba9"
down_revision: Union[str, None] = "85a2bf6daf97"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users", "timezone", existing_type=postgresql.INTERVAL(), nullable=False
    )
    op.create_unique_constraint(None, "users", ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    op.alter_column(
        "users", "timezone", existing_type=postgresql.INTERVAL(), nullable=True
    )
    # ### end Alembic commands ###
