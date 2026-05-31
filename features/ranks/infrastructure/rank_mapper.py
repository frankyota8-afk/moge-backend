from features.ranks.models import Rank
from features.ranks.domain.rank_entity import RankEntity


class RankMapper:

    def toEntity(rank : Rank )->RankEntity:
        return RankEntity(
            id=rank.id,
            rank_id=rank.rank_id,
            rank_name=rank.rank_name
        )

    def toModel(entity : RankEntity)->dict:
        return {
            "rank_id" : entity.rank_id,
            "rank_name" : entity.rank_name
        }