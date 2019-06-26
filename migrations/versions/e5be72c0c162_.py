"""empty message

Revision ID: e5be72c0c162
Revises: 63ffcb66d88f
Create Date: 2019-06-26 17:40:38.965438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5be72c0c162'
down_revision = '63ffcb66d88f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Bicycles',
    sa.Column('UserId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=64), nullable=True),
    sa.Column('Num', sa.Integer(), nullable=True),
    sa.Column('Time', sa.TIMESTAMP(), nullable=True),
    sa.Column('Address', sa.String(length=64), nullable=True),
    sa.Column('Photo', sa.String(length=64), nullable=True),
    sa.Column('City', sa.String(length=64), nullable=True),
    sa.Column('Detail', sa.String(length=64), nullable=True),
    sa.Column('Handler', sa.String(length=64), nullable=True),
    sa.Column('Status', sa.String(length=64), nullable=True),
    sa.Column('Score', sa.Integer(), nullable=True),
    sa.Column('Updatedate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('UserId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Bicycles')
    # ### end Alembic commands ###
