"""initial revision

Revision ID: 7bf16e0ea6bf
Revises: Dima
Create Date: 2018-12-16 16:04:09.065826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bf16e0ea6bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'warranty',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('start_date', sa.Date, nullable=False),
        sa.Column('end_date', sa.Date, nullable=False)
    )


def downgrade():
    pass
