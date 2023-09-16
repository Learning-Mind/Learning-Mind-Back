from app.models.sql import Memo
from app.repository.base import BaseDataManager
from app.schema.memo import MemoSchema


class MemoDataManager(BaseDataManager):
    async def create_memo(self, memo: Memo):
        model = await self.add_one(memo)
        return MemoSchema(**model.to_dict())