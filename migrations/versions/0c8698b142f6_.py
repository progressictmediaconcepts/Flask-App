"""empty message

Revision ID: 0c8698b142f6
Revises: 692ee9902b23
Create Date: 2022-08-25 08:28:25.940872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c8698b142f6'
down_revision = '692ee9902b23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(length=120), nullable=False))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=120), nullable=False))
    op.drop_column('Artist', 'website')
    op.add_column('Venue', sa.Column('website_link', sa.String(length=120), nullable=False))
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=False))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=120), nullable=False))
    op.drop_column('Venue', 'website')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'genres')
    op.drop_column('Venue', 'website_link')
    op.add_column('Artist', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###