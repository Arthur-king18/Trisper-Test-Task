"""third

Revision ID: 4d69091f5eb4
Revises: cbd2f9b025a5
Create Date: 2023-07-30 12:45:02.717067

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4d69091f5eb4'
down_revision = 'cbd2f9b025a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prompt_history',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('prompt', sa.Unicode(length=255), nullable=False),
        sa.Column('user_id', sa.BigInteger(), nullable=True),
        sa.Column('presentation_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['presentation_id'], ['presentations.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('promt_history')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('promt_history',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('promt', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('presentation_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['presentation_id'], ['presentations.id'], name='promt_history_presentation_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='promt_history_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='promt_history_pkey')
    )
    op.drop_table('prompt_history')
    # ### end Alembic commands ###
