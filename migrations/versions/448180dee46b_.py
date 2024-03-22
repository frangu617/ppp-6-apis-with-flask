"""empty message

Revision ID: 448180dee46b
Revises: c5da839cf9af
Create Date: 2024-03-22 11:52:58.205480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '448180dee46b'
down_revision = 'c5da839cf9af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reptiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('reptile_type', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('facts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('reptile_type', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='facts_pkey')
    )
    op.drop_table('reptiles')
    # ### end Alembic commands ###