# ProgressBar

A simple tool to view the progress of a loop in your notebook.

## Usage

Integrate the progress bar into your loop in the following way.

```python
seconds = 10

# Create a progress bar
p = ProgressBar(total=seconds, width=10)

for i in range(seconds):
    
    # Update and draw the bar
    p.update(i)
    p.draw()
    if i == 5:
        # Output a message
        p.message("We're halfway! 5 seconds to go...")
    
    # Do something useful
    time.sleep(1)

# Mark process as done.
p.end()
```