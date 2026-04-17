import plotly.graph_objects as go

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [42000, 47500, 51200, 55800, 61300, 68900]

fig = go.Figure()
fig.add_trace(go.Scatter(x=months, y=revenue, mode="lines+markers",
    line=dict(color="#00ccff", width=3), name="Revenue"))
fig.update_layout(
    title="Monthly Revenue Dashboard",
    paper_bgcolor="#0d1117", plot_bgcolor="#0d1117",
    font=dict(color="white"), showlegend=True)
fig.write_html("dashboard.html")
print("Dashboard saved: dashboard.html")
