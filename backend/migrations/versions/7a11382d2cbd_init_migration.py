"""init migration

Revision ID: 7a11382d2cbd
Revises: 
Create Date: 2020-06-25 00:52:11.805004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a11382d2cbd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('status')
    )
    op.create_table('org_unit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('province', sa.String(length=45), nullable=False),
    sa.Column('district', sa.String(length=45), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('contact', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('status')
    )
    op.create_table('province',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('telephone', sa.String(length=10), nullable=False),
    sa.Column('first_name', sa.String(length=45), nullable=False),
    sa.Column('last_name', sa.String(length=45), nullable=False),
    sa.Column('nic_number', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=45), nullable=True),
    sa.Column('password', sa.String(length=45), nullable=False),
    sa.Column('salt', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('telephone')
    )
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=45), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('contact', sa.String(length=10), nullable=False),
    sa.Column('password', sa.String(length=45), nullable=False),
    sa.Column('salt', sa.String(length=45), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['org_id'], ['org_unit.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('district',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('province_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['province_id'], ['province.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('alert',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('alert_type', sa.String(length=45), nullable=False),
    sa.Column('subject', sa.String(length=45), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['admin.id'], ),
    sa.ForeignKeyConstraint(['org_id'], ['org_unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('venue', sa.String(length=45), nullable=False),
    sa.Column('location_lat', sa.Float(), nullable=False),
    sa.Column('location_long', sa.Float(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('coordinator_name', sa.String(length=45), nullable=False),
    sa.Column('coordinator_contact', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['admin.id'], ),
    sa.ForeignKeyConstraint(['org_id'], ['org_unit.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['event_status.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('incident',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('province', sa.String(length=45), nullable=False),
    sa.Column('district', sa.String(length=45), nullable=False),
    sa.Column('city', sa.String(length=45), nullable=False),
    sa.Column('location_lat', sa.Float(), nullable=True),
    sa.Column('location_long', sa.Float(), nullable=True),
    sa.Column('patient_name', sa.String(length=45), nullable=False),
    sa.Column('patient_gender', sa.String(length=1), nullable=False),
    sa.Column('patient_dob', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('reported_time', sa.DateTime(), nullable=False),
    sa.Column('reported_user_id', sa.Integer(), nullable=False),
    sa.Column('patient_status_id', sa.Integer(), nullable=False),
    sa.Column('is_verified', sa.Integer(), nullable=False),
    sa.Column('verified_by', sa.Integer(), nullable=True),
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['org_id'], ['org_unit.id'], ),
    sa.ForeignKeyConstraint(['patient_status_id'], ['patient_status.id'], ),
    sa.ForeignKeyConstraint(['reported_user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['verified_by'], ['admin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('incident')
    op.drop_table('event')
    op.drop_table('alert')
    op.drop_table('district')
    op.drop_table('admin')
    op.drop_table('user')
    op.drop_table('province')
    op.drop_table('patient_status')
    op.drop_table('org_unit')
    op.drop_table('event_status')
    # ### end Alembic commands ###