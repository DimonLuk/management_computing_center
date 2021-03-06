"""empty message

Revision ID: 19974c57241b
Revises: 
Create Date: 2018-12-23 04:17:40.500792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19974c57241b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manufacturer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=500), nullable=False),
    sa.Column('phone_number', sa.String(length=13), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('warranty',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('componentmetainfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('serial_number', sa.String(length=10), nullable=False),
    sa.Column('manufacturer_id', sa.Integer(), nullable=True),
    sa.Column('warranty_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['manufacturer_id'], ['manufacturer.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['warranty_id'], ['warranty.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('motherboard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('form_factor', sa.String(length=10), nullable=False),
    sa.Column('chipset', sa.String(length=10), nullable=False),
    sa.Column('pci_slots', sa.Integer(), nullable=False),
    sa.Column('used_pci_slots', sa.Integer(), nullable=False),
    sa.Column('ram_slots', sa.Integer(), nullable=False),
    sa.Column('used_ram_slots', sa.Integer(), nullable=False),
    sa.Column('component_meta_info_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['component_meta_info_id'], ['componentmetainfo.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('processor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cores', sa.Integer(), nullable=False),
    sa.Column('l1_cache', sa.Integer(), nullable=False),
    sa.Column('l2_cache', sa.Integer(), nullable=False),
    sa.Column('l3_cache', sa.Integer(), nullable=False),
    sa.Column('component_meta_info_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['component_meta_info_id'], ['componentmetainfo.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ram',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('frequency', sa.Integer(), nullable=False),
    sa.Column('component_meta_info_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['component_meta_info_id'], ['componentmetainfo.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trunk',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('width', sa.Numeric(precision=8), nullable=False),
    sa.Column('height', sa.Numeric(precision=8), nullable=False),
    sa.Column('form_factor', sa.String(length=10), nullable=False),
    sa.Column('component_meta_info_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['component_meta_info_id'], ['componentmetainfo.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('computer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room', sa.String(length=10), nullable=False),
    sa.Column('trunk_id', sa.Integer(), nullable=True),
    sa.Column('motherboard_id', sa.Integer(), nullable=True),
    sa.Column('ram_id', sa.Integer(), nullable=True),
    sa.Column('processor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['motherboard_id'], ['motherboard.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['processor_id'], ['processor.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ram_id'], ['ram.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['trunk_id'], ['trunk.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('computer')
    op.drop_table('trunk')
    op.drop_table('ram')
    op.drop_table('processor')
    op.drop_table('motherboard')
    op.drop_table('componentmetainfo')
    op.drop_table('warranty')
    op.drop_table('manufacturer')
    # ### end Alembic commands ###
