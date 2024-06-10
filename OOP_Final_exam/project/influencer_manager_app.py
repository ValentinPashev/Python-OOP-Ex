from typing import List

from project import BaseCampaign
from project import HighBudgetCampaign
from project import LowBudgetCampaign
from project import BaseInfluencer
from project import PremiumInfluencer
from project import StandardInfluencer


class InfluencerManagerApp:

    VALID_INFLUENCERS = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }

    VALID_CAMPAIGNS = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []  # list with influences as objects
        self.campaigns: List[BaseCampaign] = []  # list with campaigns as objects

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCERS.keys():
            return f"{influencer_type} is not an allowed influencer type."

        try:
            influencer = [i for i in self.influencers if i.username == username][0]
            return f"{influencer.username} is already registered."

        except IndexError:
            new_influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
            self.influencers.append(new_influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):

        if campaign_type not in self.VALID_CAMPAIGNS.keys():
            return f"{campaign_type} is not a valid campaign type."

        try:
            campaign = [c for c in self.campaigns if c.campaign_id == campaign_id][0]
            return f"Campaign ID {campaign.campaign_id} has already been created."

        except IndexError:
            new_campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(new_campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):

        try:
            current_influencer = [i for i in self.influencers if i.username == influencer_username][0]

        except IndexError:
            return f"Influencer '{influencer_username}' not found."

        try:
            current_campaign = [c for c in self.campaigns if c.campaign_id == campaign_id][0]

        except IndexError:
            return f"Campaign with ID {campaign_id} not found."

        if not current_campaign.check_eligibility(current_influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = current_influencer.calculate_payment(current_campaign)

        if payment > 0:
            current_campaign.approved_influencers.append(current_influencer)
            current_campaign.budget -= payment
            current_influencer.campaigns_participated_in.append(current_campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_followers_as_dict = {}
        for campaign in self.campaigns:
            total_followers_as_dict[campaign] = sum(
                influencer.reached_followers(campaign.__class__.__name__) for influencer in
                campaign.approved_influencers)

    def influencer_campaign_report(self, username: str):
        influencer_names_for_report = None
        for i in self.influencers:
            if i.username == username:
                influencer_names_for_report = i
                break
        if not influencer_names_for_report:
            return f"{username} has not participated in any campaigns."

        return influencer_names_for_report.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))
        statistics_as_list = []
        for campaign in sorted_campaigns:
            total_reached_followers = sum(influencer.reached_followers(campaign.__class__.__name__) for influencer in
                                          campaign.approved_influencers)
            statistics_as_list.append(
                f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}")

        return "$$ Campaign Statistics $$\n" + "\n".join(statistics_as_list)



























