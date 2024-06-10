from project import BaseCampaign
from project import BaseInfluencer


class StandardInfluencer(BaseInfluencer):

    PAYMENT_PERCENTAGE = 0.45

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        return self.PAYMENT_PERCENTAGE * campaign.budget

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.2)
        elif campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.9)
        else:
            raise ValueError("Invalid campaign type.")