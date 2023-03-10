"""empty message

Revision ID: a94ffb827482
Revises: b556cd8025f0
Create Date: 2022-12-05 10:16:22.738303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a94ffb827482'
down_revision = 'b556cd8025f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
