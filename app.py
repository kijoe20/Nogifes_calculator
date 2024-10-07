import streamlit as st
from datetime import datetime, timedelta

# Function to calculate recovery time
def calculate_recovery_time(max_lp, current_lp):
    recover_time = (max_lp - current_lp) * 4  # 4 minutes per LP
    hours = recover_time // 60
    minutes = recover_time % 60
    return hours, minutes

# Function to update current time
# Main app logic
def main():
    """Main app logic"""

    # Streamlit app layout
    st.write("### LP Recovery Calculator")

    max_lp = st.number_input("Maximum LP", min_value=0, value=80, help="Enter the maximum LP achievable.")
    current_lp = st.number_input("Current LP", min_value=0, value=0, help="Enter your current LP.")

    # Calculate Button
    if st.button("Calculate"):
        calculate_recovery_time(max_lp, current_lp)

    #Display current time
    current_time = datetime.now()
    st.write("Current time:", current_time.strftime("%H:%M"))
    
    # LP recovery time calculation
    if current_lp < 0 or max_lp < 0:
        st.error("LP values cannot be negative.")
    elif current_lp > max_lp:
        st.error("Current LP cannot be greater than Maximum LP.")
    else:
        hours, minutes = calculate_recovery_time(max_lp, current_lp)
        recover_time_str = f"**{hours}h {minutes}m**"
        st.write("LP Recover time:", recover_time_str)

        # Estimated time of LP full recovery
        recover_time = timedelta(hours=hours, minutes=minutes)
        estimated_finish_time = current_time + recover_time
        st.write("Estimated time of LP full recovery:", estimated_finish_time.strftime("**%H:%M**"))

    #line break
    st.write("---")
    st.write("### Total LP Recovery")

    # 2 columns for input
    col1, col2 = st.columns(2)
    with col1:
        duration_days = st.number_input(
            "Duration (days)", min_value=0, value=1, help="Enter the duration for LP recovery (in days)."
        )
    with col2:
        duration_hours = st.number_input(
            "Duration (hours)", min_value=0, value=0, help="Enter the duration for LP recovery (in hours)."
        )
    # Total LP recovery calculation
    total_lp_recovery = (duration_days * 24 + duration_hours) * 60 // 4
    st.write(f"Total LP recovery over {duration_days} day(s) and {duration_hours} hour(s): **{total_lp_recovery} LP**")

# Run the app
if __name__ == "__main__":
    main()

