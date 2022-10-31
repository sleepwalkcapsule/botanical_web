"""added email to user

Revision ID: 46500bd04581
Revises: ecb48b7e1d99
Create Date: 2022-10-31 12:49:13.681310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46500bd04581'
down_revision = 'ecb48b7e1d99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###