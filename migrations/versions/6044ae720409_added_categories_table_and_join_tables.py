"""added categories table and join tables

Revision ID: 6044ae720409
Revises: 1ea2428814ff
Create Date: 2020-11-23 16:53:52.840295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6044ae720409'
down_revision = '1ea2428814ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('leagues_categories',
    sa.Column('league_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['league_id'], ['leagues.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leagues_categories')
    op.drop_table('categories')
    # ### end Alembic commands ###
