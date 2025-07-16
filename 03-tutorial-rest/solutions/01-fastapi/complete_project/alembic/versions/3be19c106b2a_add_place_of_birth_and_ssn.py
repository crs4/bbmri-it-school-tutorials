"""add place of birth and ssn

Revision ID: 3be19c106b2a
Revises: 6c6fad006424
Create Date: 2025-07-07 12:27:46.779231

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import random
from codicefiscale import codicefiscale


# revision identifiers, used by Alembic.
revision: str = "3be19c106b2a"
down_revision: Union[str, Sequence[str], None] = "6c6fad006424"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

COMUNI = [
    "Roma",
    "Milano",
    "Napoli",
    "Torino",
    "Palermo",
    "Genova",
    "Bologna",
    "Firenze",
    "Cagliari",
    "Bari",
    "Venezia",
]


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "participants",
        sa.Column(name="place_of_birth", type_=sa.String, nullable=True),
        schema="biobank_manager",
    )
    op.add_column(
        "participants",
        sa.Column(name="ssn", type_=sa.String, nullable=True),
        schema="biobank_manager",
    )
    # add values to existing participants

    conn = op.get_bind()
    # Fetch all person IDs
    results = conn.execute(
        sa.text(
            "SELECT id, last_name, first_name, gender, date_of_birth FROM biobank_manager.participants"
        )
    ).fetchall()

    # Assign a random city to each
    for row in results:
        city = random.choice(COMUNI)
        conn.execute(
            sa.text(
                "UPDATE biobank_manager.participants SET place_of_birth = :city WHERE id = :id"
            ),
            {"city": city, "id": row.id},
        )
        # Add SSN based on existing data
        ggender = row.gender
        print(f"row.gender is {row.gender}")
        if row.gender not in ["M", "F"]:
            ggender = random.choice(["M", "F"])
        ssn = codicefiscale.encode(
            lastname=row.last_name,
            firstname=row.first_name,
            gender=ggender,
            birthdate=str(row.date_of_birth),
            birthplace=city,
        )
        conn.execute(
            sa.text(
                "UPDATE biobank_manager.participants SET ssn = :ssn WHERE id = :id"
            ),
            {"ssn": ssn, "id": row.id},
        )

    op.alter_column(
        "participants", "place_of_birth", nullable=False, schema="biobank_manager"
    )
    op.alter_column("participants", "ssn", nullable=False, schema="biobank_manager")


def downgrade() -> None:
    """Downgrade schema."""
    pass
