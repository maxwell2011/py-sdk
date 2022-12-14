"""
Log Request Model

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/LogRequest.ts
"""

"""
import BaseModel from '@/models/utils/BaseModel';
"""
from .utils import BaseModel

class LogRequest(BaseModel):
    """
    export default class LogRequest extends BaseModel {
        url!:       string;
        method!:    string;
        status!:    number;
        auth!:      string;
        remoteIp!:  string;
        userIp!:    string;
        referer!:   string;
        userAgent!: string;
        meta!:      null|{ [key: string]: any };
    }
    """
    def __init__(self, data: dict = {}):
        self.load(data)

    def __repr__(self):
        return f'<LogRequest url={self.url} \
                             method={self.method} \
                             status={self.status} \
                             auth={self.auth} \
                             remote_ip={self.remote_ip} \
                             user_ip={self.user_ip} \
                             referer={self.referer} \
                             user_agent={self.user_agent} \
                             meta={self.meta}>'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.url == other.url and \
               self.method == other.method and \
               self.status == other.status and \
               self.auth == other.auth and \
               self.remote_ip == other.remote_ip and \
               self.user_ip == other.user_ip and \
               self.referer == other.referer and \
               self.user_agent == other.user_agent and \
               self.meta == other.meta

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.url, self.method, self.status, self.auth, self.remote_ip, self.user_ip, self.referer, self.user_agent, self.meta))

    def to_dict(self) -> dict:
        super().to_dict()
        return {
            'url': self.url,
            'method': self.method,
            'status': self.status,
            'auth': self.auth,
            'remoteIp': self.remote_ip,
            'userIp': self.user_ip,
            'referer': self.referer,
            'userAgent': self.user_agent,
            'meta': self.meta,
            **self._base_dict
        }

    @classmethod
    def from_dict(cls, data: dict):
        data['url'] = data.get('url', '')
        data['method'] = data.get('method', 'GET')
        data['status'] = data.get('status', 200)
        data['auth'] = data.get('auth', 'guest')
        data['remoteIp'] = data.get('remoteIp', '')
        data['userIp'] = data.get('userIp', '')
        data['referer'] = data.get('referer', '')
        data['userAgent'] = data.get('userAgent', '')
        data['meta'] = data.get('meta', {})
        return cls(data)

    def load(self, data: dict):
        """
        load(data: { [key: string]: any }) {
            super.load(data);

            // fallback to the ip field for backward compatability
            data.remoteIp = data.remoteIp || data.ip;

            this.url       = typeof data.url === 'string' ? data.url : '';
            this.method    = typeof data.method === 'string' ? data.method : 'GET';
            this.status    = typeof data.status === 'number' ? data.status : 200;
            this.auth      = typeof data.auth === 'string' ? data.auth : 'guest';
            this.remoteIp  = typeof data.remoteIp === 'string' ? data.remoteIp : '';
            this.userIp    = typeof data.userIp === 'string' ? data.userIp : '';
            this.referer   = typeof data.referer === 'string' ? data.referer : '';
            this.userAgent = typeof data.userAgent === 'string' ? data.userAgent : '';
            this.meta      = typeof data.meta === 'object' && data.meta !== null ? data.meta : {};
        }
        """
        super().load(data)

        # fallback to the ip field for backward compatability
        data['remoteIp'] = data['remoteIp'] or data['ip']

        self.url = data.get('url', '')
        self.method = data.get('method', 'GET')
        self.status = data.get('status', 200)
        self.auth = data.get('auth', 'guest')
        self.remote_ip = data.get('remoteIp', '')
        self.user_ip = data.get('userIp', '')
        self.referer = data.get('referer', '')
        self.user_agent = data.get('userAgent', '')
        self.meta = data.get('meta', {})
        
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