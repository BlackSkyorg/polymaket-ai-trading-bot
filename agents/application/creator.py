from agents.application.executor import Executor as Agent
from agents.polymarket.gamma import GammaMarketClient as Gamma
from agents.polymarket.polymarket import Polymarket


class Creator:
    def __init__(self):
        self.polymarket = Polymarket()
        self.gamma = Gamma()
        self.agent = Agent()
    def one_best_market(self):
        """
        one_best_trade is a strategy that evaluates all events, markets, and orderbooks

        leverages all available information sources accessible to the autonomous agent

        then executes that trade without any human intervention

        """
        try:
            events = self.polymarket.get_all_tradeable_events()

            filtered_events = self.agent.filter_events_with_rag(events)

            markets = self.agent.map_filtered_events_to_markets(filtered_events)

            filtered_markets = self.agent.filter_markets(markets)

            best_market = self.agent.source_best_market_to_create(filtered_markets)
            return best_market

        except Exception as e:
            self.one_best_market()

    def maintain_positions(self):
        pass

    def incentive_farm(self):
        pass
if __name__ == "__main__":
    c = Creator()
    c.one_best_market()
