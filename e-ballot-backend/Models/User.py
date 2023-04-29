"""
This File Contains the User Model
"""
# Python Imports:
from __future__ import annotations
from typing import Optional
from bson import ObjectId

# Imports
from data_manager.e_ballot_db import E_BALLOT_DB


class User:
    class Profile:

        first_name: str
        last_name: str

        def __init__(self, first_name: str, last_name: str) -> None:
            self.first_name = first_name
            self.last_name = last_name

        @staticmethod
        def from_json(doc: dict) -> User.Profile:
            return User.Profile(
                first_name=doc['first_name'],
                last_name=doc['last_name'],
            )

        def to_json(self) -> dict:
            return \
                {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                }

    # ===================================

    oid: ObjectId
    profile: User.Profile

    def __init__(self, oid: ObjectId, profile: User.Profile) -> None:
        self.oid = oid
        self.profile = profile

    def to_json(self) -> dict:
        return \
            {
                '_id': self.oid,
                'profile': self.profile.to_json(),
            }

    @staticmethod
    def from_json(doc: dict) -> User:
        return User(
            oid=doc['_id'],
            profile=User.Profile.from_json(doc['profile']),
        )

    def __repr__(self) -> str:
        return f'User: {self.profile.first_name} {self.profile.last_name}'