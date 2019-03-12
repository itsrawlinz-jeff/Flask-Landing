"""empty message

Revision ID: d64db672b5ce
Revises: 0bc39a029870
Create Date: 2019-03-11 15:46:47.427682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd64db672b5ce'
down_revision = '0bc39a029870'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('email_signup', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.add_column('email_signup', sa.Column('updated', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_email_signup_timestamp'), 'email_signup', ['timestamp'], unique=False)
    op.create_index(op.f('ix_email_signup_updated'), 'email_signup', ['updated'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_email_signup_updated'), table_name='email_signup')
    op.drop_index(op.f('ix_email_signup_timestamp'), table_name='email_signup')
    op.drop_column('email_signup', 'updated')
    op.drop_column('email_signup', 'timestamp')
    # ### end Alembic commands ###