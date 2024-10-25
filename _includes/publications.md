<script>
  let activeBlock = null; // To keep track of the currently active block

  // Show publications based on type
  function showPublications(type) {
    const allItems = document.querySelectorAll('.pub-item');

    // Show or hide items based on the type
    allItems.forEach(item => {
      const itemTypes = item.getAttribute('data-type').split(',');
      if (type === 'all' || itemTypes.includes(type)) {
        item.style.display = 'block'; // Show matching items
      } else {
        item.style.display = 'none'; // Hide non-matching items
      }
    });
  }

  // Function to handle mouse enter and keep the active type
  function handleMouseEnter(block) {
    // Remove the active class from the previously active block
    if (activeBlock) {
      activeBlock.classList.remove('active');
    }
    
    // Set the current block as active and show its publications
    activeBlock = block;
    activeBlock.classList.add('active');
    showPublications(block.getAttribute('data-type')); // Show publications for the active type
  }

  // Show all publications by default on page load
  window.onload = function() {
    showPublications('all');
  };
</script>

<!-- CSS to style the filter blocks and publication items -->
<style>
  .pub-type-filter {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 20px;
  }

  .pub-type {
    width: 80px; /* Set a fixed width for all blocks */
    height: 26px; /* Set a fixed height */
    line-height: 24px; /* Vertically center the text */
    background-color: #f1f1f1;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;
    font-weight: bold;
    transition: background-color 0.3s ease;
    margin-right: 10px;
    border: 2px solid transparent;
  }

  .pub-type[data-type="all"] {
      background-color: #aadaac; /* Green */
      /*color: #4CAF50;*/
  }
    
  .pub-type[data-type="mllm"] {
      background-color: #f4a286; /* Blue */
  }
    
  .pub-type[data-type="genai"] {
      background-color: #9abcec; /* Orange */
  }

/* Hover state */
.pub-type:hover {
  opacity: 0.8; /* Slight transparency on hover */
}

/* Active class for keeping the border color */
.active {
  border-color: inherit; /* Retain the inherited border color */
}

/* Change background and text color on hover */
.pub-type[data-type="all"]:hover,
.active[data-type="all"] {
  background-color: #4dae50; /* Darker green */
  color: #e0e0e0; /* Light gray text */
}

.pub-type[data-type="mllm"]:hover,
.active[data-type="mllm"] {
  background-color: #e64a19; /* Darker blue */ 
  color: white; /* White text */
}

.pub-type[data-type="genai"]:hover,
.active[data-type="genai"] {
  background-color: #1e88e5; /* Darker orange */
  color: white; /* White text */
}

  .pub-item {
    display: none; /* Initially hidden */
  }
</style>

<br>
<h2 id="publications" style="margin: 2px 0px -15px;">Publications <temp style="font-size:15px;">[</temp><a href="https://scholar.google.com/citations?hl=en&user=uToGtIwAAAAJ" target="_blank" style="font-size:15px;">Google Scholar</a><temp style="font-size:15px;">]</temp></h2>

<div class="publications">
<ol class="bibliography">

<div class="pub-type-filter">
  <div class="pub-type" data-type="all" onmouseover="showPublications('all')">All</div>
  <div class="pub-type" data-type="genai" onmouseover="showPublications('genai')">GenAI</div>
  <div class="pub-type" data-type="mllm" onmouseover="showPublications('mllm')">MLLM</div>
</div>

{% for link in site.data.publications.main %}

<li class="pub-item" data-type="{{ link.type }}">
<div class="pub-row">
  <div class="col-sm-3 abbr" style="position: relative;padding-right: 15px;padding-left: 15px;">
    {% if link.image %} 
    <img src="{{ link.image }}" playsinline="" class="teaser img-fluid z-depth-1" style="width=100;height=40%">
    {% endif %}
    {% if link.video %}
    <video poster="" id="teaser" autoplay muted loop class="teaser img-fluid z-depth-1">
    <source src="{{ link.video }}" type="video/mp4">
    </video>
    {% endif %}
    {% if link.conference_short %} 
    <abbr class="badge">{{ link.conference_short }}</abbr>
    {% endif %}
    {% if link.is_preprint %} 
    <abbrp class="badge">Preprint</abbrp>
    {% endif %}
  </div>
  <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
      <div class="title"><a href="{{ link.pdf }}">{{ link.title }}</a></div>
      <div class="author">{{ link.authors }}</div>
      <div class="periodical"><em>{{ link.conference }}</em>
      </div>
    <div class="links">
      {% if link.page %} 
      <a href="{{ link.page }}" target="_blank" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Project Page</a>
      {% endif %}
      {% if link.pdf %} 
      <a href="{{ link.pdf }}" target="_blank" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">PDF</a>
      {% endif %}
      {% if link.code %} 
      <a href="{{ link.code }}" target="_blank" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Code</a>
      {% endif %}
      {% if link.bibtex %} 
      <a href="{{ link.cbibtex }}" target="_blank" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">BibTex</a>
      {% endif %}
      {% if link.notes %} 
      <strong> &nbsp; <i style="color:#e74d3c">{{ link.notes }}</i></strong>
      {% endif %}
      {% if link.others %} 
      {{ link.others }}
      {% endif %}
    </div>
  </div>
</div>
<br>
</li>

{% endfor %}

</ol>
</div>

