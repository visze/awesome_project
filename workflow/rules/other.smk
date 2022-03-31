# An example collection of Snakemake rules imported in the main Snakefile.


rule other_sample_plot:
    conda:
        "../envs/default.yaml"
    input:
        script=getScript("plot_sample.py"),
    output:
        report("results/plots/{sample}.png", caption="../report/some-plot.rst"),
    params:
        condition=lambda wc: samples.loc[wc.sample].condition,
    log:
        "results/logs/other_sample_plot.{sample}.log",
    shell:
        """
        python {input.script} --condition {params.condition} --output {output} &> {log}
        """
