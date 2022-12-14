"""
User Model

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/User.ts
"""

"""
import BaseModel from '@/models/utils/BaseModel';
import Record    from '@/models/Record';
"""
from .utils import BaseModel
from .record import Record

class User(BaseModel):
    """
    export default class User extends BaseModel {
        email!:                  string;
        verified!:               boolean;
        lastResetSentAt!:        string;
        lastVerificationSentAt!: string;
        profile!:                null|Record;
    }
    """
    def __init__(self, data: dict = {}):
        self.load(data)

    def __repr__(self):
        return f'<User email={self.email} \
                       verified={self.verified} \
                       last_reset_sent_at={self.last_reset_sent_at} \
                       last_verification_sent_at={self.last_verification_sent_at} \
                       profile={self.profile}>'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.email == other.email and \
               self.verified == other.verified and \
               self.last_reset_sent_at == other.last_reset_sent_at and \
               self.last_verification_sent_at == other.last_verification_sent_at and \
               self.profile == other.profile

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.email, self.verified, self.last_reset_sent_at, self.last_verification_sent_at, self.profile))

    def to_dict(self) -> dict:
        super().to_dict()
        return {
            'email': self.email,
            'verified': self.verified,
            'lastResetSentAt': self.last_reset_sent_at,
            'lastVerificationSentAt': self.last_verification_sent_at,
            'profile': self.profile.to_dict() if self.profile else None,
            **self._base_dict
        }

    @classmethod
    def from_dict(cls, data: dict):
        data['email'] = data.get('email', ''),
        data['verified'] = data.get('verified', False),
        data['lastResetSentAt'] = data.get('lastResetSentAt', ''),
        data['lastVerificationSentAt'] = data.get('lastVerificationSentAt', ''),
        data['profile'] = Record.from_dict(data.get('profile', {})),
        return cls(data)

    def load(self, data: dict):
        """
        load(data: { [key: string]: any }) {
            super.load(data);

            this.email = typeof data.email === 'string' ? data.email : '';
            this.verified = !!data.verified;
            this.lastResetSentAt = typeof data.lastResetSentAt === 'string' ? data.lastResetSentAt : '';
            this.lastVerificationSentAt = typeof data.lastVerificationSentAt === 'string' ? data.lastVerificationSentAt : '';
            this.profile = data.profile ? new Record(data.profile) : null;
        }
        """
        super().load(data)

        self.email = data.get('email', '')
        self.verified = data.get('verified', False)
        self.last_reset_sent_at = data.get('lastResetSentAt', '')
        self.last_verification_sent_at = data.get('lastVerificationSentAt', '')
        self.profile = Record.from_dict(data.get('profile', {}))
        
    def clone(self) -> dict:
        """
        Robust deep clone of a model.
        clone(): BaseModel { return new (this.constructor as any)(JSON.parse(JSON.stringify(this))); }
        """
        return self.to_dict()

    def export(self) -> dict:
        """
        Exports all model properties as a new plain object.
        
        export(): { [key: string]: any } { return Object.assign({}, this); }
        """
        return self.to_dict()