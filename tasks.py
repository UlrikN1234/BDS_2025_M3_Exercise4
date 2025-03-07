# tasks.py
# Made to define the tasks that the agents will perform

from crewai import Task
from textwrap import dedent

# Defining the agent tasks
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_business_strategist(self, agent, var2):
        return Task(
            description=dedent(
                f"""
                Provide an analysis of how fiscal policies and current market trends impact business growth, with a focus on your business idea, '{var2}'.

                Use the most recent data to evaluate how these economic factors might affect your business's operations, consumer behavior, and overall market position.

                {self.__tip_section()}
            """
            ),
            expected_output="An analysis of how fiscal policies and market trends could impact the operations and profitability of the business idea '{var2}'.",
            agent=agent,
        )

    def task_2_corporate_financial_planner(self, agent, var2):
        return Task(
            description=dedent(
                f"""
                Analyze the impact of recent monetary policy decisions on business financing, considering the fiscal policy landscape provided by the Business Strategist agent.

                Focus on how these monetary policies can influence cash flow, capital investments, and the overall financial strategy for your business idea, '{var2}'.

                {self.__tip_section()}
            """
            ),
            expected_output="A financial analysis that discusses the impact of monetary policy on business financing, capital investments, and long-term profitability for '{var2}'.",
            agent=agent,
        )

    def task_3_market_researcher(self, agent, var1, var2, var3):
        return Task(
            description=dedent(
                f"""
                Conduct a market analysis to determine the target market, customer behavior, and competitive landscape for the proposed business, '{var1}'.

                Take into account the vision of your business, '{var3}', and how your business idea, '{var2}', fits into the market. Use the most recent data to identify trends, opportunities, and the competitive landscape for '{var1}'.

                {self.__tip_section()}
            """
            ),
            expected_output="A detailed market analysis highlighting trends, opportunities, and the competitive landscape for '{var1}' and its target audience.",
            agent=agent,
        )

    def task_4_operations_manager(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
                Provide insights into how to operationalize the business, '{var1}', including production processes, supply chain management, and resource allocation.

                Consider scaling challenges and operational efficiencies for '{var1}', and address any specific challenges related to the business idea '{var2}'.

                {self.__tip_section()}
            """
            ),
            expected_output="A comprehensive operations plan that addresses scaling, resource allocation, and process optimization for '{var1}'.",
            agent=agent,
        )

    def task_5_marketing_expert(self, agent, var1, var2, var3):
        return Task(
            description=dedent(
                f"""
                Develop a marketing strategy that includes customer acquisition channels, branding, and engagement strategies for the business, '{var1}'.

                Tailor the strategy to the target market, considering the vision of your business idea, '{var3}', and the specific business idea, '{var2}'.

                {self.__tip_section()}
            """
            ),
            expected_output="A marketing plan that includes customer acquisition strategies, branding, and market positioning for '{var1}'.",
            agent=agent,
        )

    def task_6_human_resources_specialist(self, agent, var1):
        return Task(
            description=dedent(
                f"""
                Provide insights into building the human resources structure for the business, '{var1}'.

                Address recruitment, employee retention, and organizational culture specific to the needs of '{var1}'.

                {self.__tip_section()}
            """
            ),
            expected_output="A human resources strategy that outlines recruitment, training, and retention efforts for the business '{var1}'.",
            agent=agent,
        )

    def task_7_legal_advisor(self, agent, var1):
        return Task(
            description=dedent(
                f"""
                Ensure that the business plan for '{var1}' adheres to all relevant laws and regulations, focusing on intellectual property, contracts, and compliance with labor laws.

                Provide insights on the legal aspects of business setup and operations for '{var1}'.

                {self.__tip_section()}
            """
            ),
            expected_output="A legal overview of the business structure, compliance, and contract management for '{var1}'.",
            agent=agent,
        )

    def task_8_technology_expert(self, agent, var1):
        return Task(
            description=dedent(
                f"""
                Advise on the technological infrastructure and tools that will support the business, '{var1}'.

                Consider automation, software, and data security needs specific to the operations of '{var1}'.

                {self.__tip_section()}
            """
            ),
            expected_output="A technology plan detailing the necessary infrastructure and tools for efficient business operations for '{var1}'.",
            agent=agent,
        )

    def task_9_business_plan_expert(self, agent, var1):
        return Task(
            description=dedent(
                f"""
                Consolidate all the insights from the economist, financial analyst, market researcher, operations manager, marketing expert, HR specialist, legal advisor, and technology expert into a comprehensive business plan for '{var1}'.

                Use the provided analyses to create a cohesive and strategic business plan that addresses all major aspects, such as market trends, operational plans, financial forecasts, legal considerations, and technology needs.

                {self.__tip_section()}
            """
            ),
            expected_output="A complete business plan for '{var1}' that integrates the insights from all the experts into a cohesive document.",
            agent=agent,
        )