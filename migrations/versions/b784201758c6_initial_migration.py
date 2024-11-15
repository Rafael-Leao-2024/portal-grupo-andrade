"""Initial migration.

Revision ID: b784201758c6
Revises: 
Create Date: 2024-11-15 18:04:13.960526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b784201758c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('image_file', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('placa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('placa', sa.String(length=80), nullable=False),
    sa.Column('renavan', sa.String(length=120), nullable=False),
    sa.Column('telefone', sa.String(length=120), nullable=False),
    sa.Column('crlv', sa.String(length=80), nullable=False),
    sa.Column('date_create', sa.DateTime(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('received', sa.Boolean(), nullable=True),
    sa.Column('received_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('placa')
    op.drop_table('user')
    # ### end Alembic commands ###
