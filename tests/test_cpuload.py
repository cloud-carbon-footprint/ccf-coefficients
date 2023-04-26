import ccfcoef.cpu_info


def test_load_check():
    cpus_amd_epyc_gen1 = ccfcoef.cpu_info.load_append_list('data/amd-epyc-gen1.csv')
    assert 'EPYC 7601' in cpus_amd_epyc_gen1
    cpus_amd_epyc_gen2 = ccfcoef.cpu_info.load_append_list('data/amd-epyc-gen2.csv')
    assert 'EPYC 7742' in cpus_amd_epyc_gen2
    cpus_amd_epyc_gen3 = ccfcoef.cpu_info.load_append_list('data/amd-epyc-gen3.csv')
    assert 'EPYC 75F3' in cpus_amd_epyc_gen3
    cpus_intel_sandybridge = ccfcoef.cpu_info.load_append_list('data/intel-sandybridge.csv')
    assert 'E5-4610' in cpus_intel_sandybridge
    cpus_intel_ivybridge = ccfcoef.cpu_info.load_append_list('data/intel-ivybridge.csv')
    assert 'E5-2609 v2' in cpus_intel_ivybridge
    cpus_intel_haswell = ccfcoef.cpu_info.load_append_list('data/intel-haswell.csv')
    assert 'E5-2630 v3' in cpus_intel_haswell
    cpus_intel_broadwell = ccfcoef.cpu_info.load_append_list('data/intel-broadwell.csv')
    assert 'E5-2683 v4' in cpus_intel_broadwell
    cpus_intel_skylake = ccfcoef.cpu_info.load_append_list('data/intel-skylake.csv')
    assert 'Platinum 8160T' in cpus_intel_skylake
    cpus_intel_cascadelake = ccfcoef.cpu_info.load_append_list('data/intel-cascadelake.csv')
    assert 'Gold 6230R' in cpus_intel_cascadelake
    cpus_intel_coffeelake = ccfcoef.cpu_info.load_append_list('data/intel-coffeelake.csv')
    assert 'E-2246G' in cpus_intel_coffeelake
