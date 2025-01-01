Key stats to focus on:
1) Basic stats:
   1) Batting Average
   2) Home Runs
   3) RBIs
2) Advanced Stats:
   5) OPS
   6) wOBA
   7) WAR
3) Underlying Stats:
   4) Exit Velo
   5) Hard Hit Rate

We will collect this data with pybaseball package. We will need:
1) Historical Batting Stats
2) Statcast Data (exit velo, launch angle)
3) Player biographical data (age, experience)
4) Ballpark Factors

--------------------------

Adding Later On:

1) Feature Engineering:
   1) Rolling Averages of Past performance
   2) Age-Related Trends
   3) Ballpark Adjustments
   4) Platoon Splits (vs left/right pitchers)
   5) Contact Quality Metrics
   6) Changes in Approach (Pull %, Ground ball %)
2) Special Considerations:
   1) Playing Time Projections
   2) Injury History
   3) Team Context
   4) League Wide Offensive Environment
   5) New Ball Specs/Rule Changes
3) Model Building
   1) Start with Basic Stats
   2) Use 3-5 Years of Historical Data
   3) Account for Partial Seasons
   4) Consider Using Different Models for Different Stats
   5) Implement Confidence Intervals