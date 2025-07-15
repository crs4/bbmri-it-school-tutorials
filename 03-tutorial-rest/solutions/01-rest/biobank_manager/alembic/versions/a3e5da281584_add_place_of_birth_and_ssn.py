"""add place of birth and ssn

Revision ID: a3e5da281584
Revises: 1227802f7ccb
Create Date: 2025-07-03 10:54:20.424120

"""

import random
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from codicefiscale import codicefiscale

# revision identifiers, used by Alembic.
revision: str = "a3e5da281584"
down_revision: Union[str, Sequence[str], None] = "1227802f7ccb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


ITALIAN_CITIES = [
    "Roma",
    "Milano",
    "Napoli",
    "Cagliari",
    "Torino",
    "Palermo",
    "Genova",
    "Bologna",
    "Firenze",
    "Bari",
    "Catania",
    "Sassari",
]

def upgrade() -> None:
    # Add nullable column
    op.add_column(
        "participants",
        sa.Column(name="place_of_birth", type_=sa.String, nullable=True),
        schema="biobank_manager",
    )

    op.add_column(
        "participants",
        sa.Column(name="ssn", type_=sa.String(16), nullable=True),
        schema="biobank_manager",
    )

    conn = op.get_bind()
    # Fetch all person IDs
    results = conn.execute(
        sa.text("SELECT id, last_name, first_name, gender, date_of_birth FROM biobank_manager.participants")
    ).fetchall()

    # Assign a random city to each 
    for row in results:
        city = random.choice(ITALIAN_CITIES)
        ssn = codicefiscale.encode(
            lastname=row.last_name,
            firstname=row.first_name,
            gender=row.gender,
            birthdate=row.date_of_birth.strftime("%m/%d/%Y"),
            birthplace=city,
        )
        conn.execute(
            sa.text("UPDATE biobank_manager.participants SET place_of_birth = :city, ssn = :ssn WHERE id = :id"),
            {"city": city, "ssn": ssn, "id": row.id},
        )

    op.alter_column('participants', 'place_of_birth', nullable=False, schema='biobank_manager')
    op.alter_column('participants', 'ssn', nullable=False, schema='biobank_manager')



def downgrade() -> None:
    """Downgrade schema."""
    pass
