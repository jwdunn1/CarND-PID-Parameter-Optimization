def twiddle(tol=1e-07): #1e-09
    p = [0.86933, 8.785924, 0.014547] # 9.251893197616131e-11   16 iters
    dp = [p[0]/10, p[1]/10, p[2]/10]

    robot = make_robot()
    _, _, best_err = run(robot, p)
    n = 0
    while sum(dp) > tol:
        print(n, "#######################################################################")
        print(p)
        print(dp)
        for i in range(len(p)):
            p[i] += dp[i]
            robot = make_robot()
            _, _, err = run(robot, p)
            if err < best_err:
                best_err = err
                dp[i] *= 1.724
            else:
                p[i] -= 2.0 * dp[i]
                robot = make_robot()
                _, _, err = run(robot, p)
                if err < best_err:
                    best_err = err
                    dp[i] *= 1.724
                else:
                    p[i] += dp[i]
                    dp[i] *= 0.276
        n += 1
    print(p, best_err)
    return p, best_err
