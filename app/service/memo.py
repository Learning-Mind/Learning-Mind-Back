from app.models.sql import Memo
from app.repository.memo import MemoDataManager
from app.schema.memo import CreateMemoSchema, MemoSchema
from app.service.base import BaseService


class MemoService(BaseService):
    async def create_memo(self, memo: CreateMemoSchema):
        return await MemoDataManager(self.session).create_memo(
            Memo(
                contents=memo.contents,
            )
        )
