"""empty message

Revision ID: f1514b012a0d
Revises: adaa7107f2b8
Create Date: 2019-07-21 14:31:23.523233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1514b012a0d'
down_revision = 'adaa7107f2b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UserMsg',
    sa.Column('user_id', sa.String(length=64), nullable=False),
    sa.Column('user_msg', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UserMsg')
    # ### end Alembic commands ###
