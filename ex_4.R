library(tidyverse)

# 1. Load and clean dataset
df <- read.csv("D:/College/Lab/DEV/students_dataset_ex_4.csv") %>% 
  na.omit() %>% 
  distinct()

# 2. Filter and summarize average marks by department
avg_marks <- df %>%
  filter(CGPA > 7.5) %>%
  group_by(Department) %>%
  summarise(Mean_Final_Marks = mean(Final_Marks))

# 3. Display summary
print(avg_marks)

# 4. Simple Bar Chart
ggplot(avg_marks, aes(x = Department, y = Mean_Final_Marks, fill = Department)) +
  geom_col(width = 0.5) +
  labs(title = "Average Final Marks by Department", x = "Department", y = "Mean Final Marks") +
  theme_minimal()