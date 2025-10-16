
<br>
<h2 id="publications" style="margin: 2px 0px -15px;">Selected Publications <temp style="font-size:15px;">[</temp><a href="https://scholar.google.com/citations?hl=en&user=uToGtIwAAAAJ" target="_blank" style="font-size:15px;">Google Scholar</a><temp style="font-size:15px;">]</temp></h2>

<div class="publications">
<ol class="bibliography">
<!--
<div class="pub-type-filter">
  <div class="pub-type" data-type="all" onmouseover="showPublications('all')">All</div>
  <div class="pub-type" data-type="genai" onmouseover="showPublications('genai')">GenAI</div>
  <div class="pub-type" data-type="mllm" onmouseover="showPublications('mllm')">MLLM</div>
</div>
-->

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

