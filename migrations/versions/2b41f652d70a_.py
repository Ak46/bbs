"""empty message

Revision ID: 2b41f652d70a
Revises: 
Create Date: 2018-04-04 19:43:25.518106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b41f652d70a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('keywords', sa.String(length=100), nullable=True),
    sa.Column('master', sa.String(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('img_src', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('create_time', sa.Integer(), nullable=True),
    sa.Column('author', sa.Text(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('len_comment', sa.Integer(), nullable=True),
    sa.Column('user_img', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['nodes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Text(), nullable=True),
    sa.Column('comment', sa.String(length=200), nullable=True),
    sa.Column('create_time', sa.Integer(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('blogs')
    op.drop_table('users')
    op.drop_table('nodes')
    # ### end Alembic commands ###
