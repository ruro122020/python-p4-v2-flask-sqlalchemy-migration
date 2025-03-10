"""rename address

Revision ID: 733ede6316d6
Revises: 5ff914638863
Create Date: 2024-01-25 16:47:31.945834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '733ede6316d6'
down_revision = '5ff914638863'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address', new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')
    # ### end Alembic commands ###
