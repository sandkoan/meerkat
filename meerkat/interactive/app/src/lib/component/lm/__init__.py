from meerkat.interactive import Box

from ..abstract import Component


class SchemaTree(Component):

    name = "SchemaTree"

    def __init__(
        self,
        df: Box,
    ) -> None:
        super().__init__()
        self.df = df

    @property
    def props(self):
        return {
            "df": self.df.config,
        }
