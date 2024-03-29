"""empty message

Revision ID: 950ba8ce1764
Revises: ec62d7ca28be
Create Date: 2019-08-07 18:21:31.048402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '950ba8ce1764'
down_revision = 'ec62d7ca28be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userdata',
    sa.Column('user_id', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('bicycles',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=64), nullable=True),
    sa.Column('time', sa.TIMESTAMP(), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=True),
    sa.Column('photo', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('detail', sa.String(length=64), nullable=True),
    sa.Column('handler', sa.String(length=64), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('updatedate', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['userdata.user_id'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bicycles')
    op.drop_table('userdata')
    # ### end Alembic commands ###
