---
title: "Eda And Visualization - Lecture Notes"
---
# Module 10: Exploratory Data Analysis & Visualization
## Instructor Lecture Notes

> Weeks 13–14 | CLO-3 | Reference: McKinney Ch 9 & Ch 13

---

### Session Objectives
- [ ] Perform EDA using descriptive statistics.
- [ ] Create and configure plots using Matplotlib pyplot.
- [ ] Build common chart types: bar, pie, box, histogram, line, scatter, heatmap.
- [ ] Introduce Seaborn and Plotly for enhanced visuals.

---

### What is EDA?

Exploratory Data Analysis is the process of examining datasets to summarize their main characteristics, often using visualizations, before formal modeling.

---

### Visualization Libraries

| Library | Strength | Use Case |
|:---|:---|:---|
| **Matplotlib** | Full control, highly customizable | Publication-quality static plots |
| **Seaborn** | Built on Matplotlib, prettier defaults | Statistical plots, heatmaps |
| **Plotly** | Interactive, web-based charts | Dashboards, presentations |

```python
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px  # optional
```

---

### Creating Plots with pyplot

```python
plt.figure(figsize=(8, 4))
plt.plot(x_data, y_data, marker="o", label="Series 1")
plt.title("Chart Title")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
```

**Markers:** `"o"` (circle), `"s"` (square), `"^"` (triangle), `"D"` (diamond)

---

### Common Chart Types

#### Line Chart
```python
plt.plot(months, revenue, marker="o")
```
**Use:** Trends over time.

#### Bar Chart
```python
plt.bar(categories, values)
plt.barh(categories, values)    # Horizontal
```
**Use:** Comparing quantities across categories.

#### Pie Chart
```python
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
```
**Use:** Proportions of a whole.

#### Histogram
```python
plt.hist(data, bins=20, edgecolor="black")
```
**Use:** Distribution of continuous data.

#### Box Plot
```python
plt.boxplot(data)
# Or with Seaborn:
sns.boxplot(x="Category", y="Value", data=df)
```
**Use:** Spread, median, quartiles, outliers.

#### Scatter Plot
```python
plt.scatter(x, y, c=colors, s=sizes)
```
**Use:** Relationship between two variables.

#### Heatmap (Seaborn)
```python
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
```
**Use:** Correlation matrix, frequency tables.

---

### Instructor Notes
- Start with Matplotlib basics (line, bar), then introduce Seaborn for box plots and heatmaps.
- Plotly is optional but generates student excitement — show one interactive chart.
- Lab Assignment 13 should cover: loading a dataset, creating at least 3 different chart types, adding titles/labels/legends.
- Reference: McKinney Ch 9 (Plotting and Visualization), Ch 13 (Data Analysis Examples).
